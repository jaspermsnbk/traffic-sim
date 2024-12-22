# Traffic Sim
#### Jasper Mesenbrink

General Problem: I hate traffic. can I help improve the infrastructure or is it a driving behaviour issue? How do I accurately model traffic at each intersection and as a whole network with different levels of flow?

## prototyping phase 1

Split traffic into 2 problems

### problem 1

for C given connections, L given lanes in each connection, and average flow, what is the optimal intersection type?

### general Flow Control types

**No Control**: traffic flows without stopping. can be combined with stop sign or yield sign. 

**Stop Sign**: must stop completely at sign before continuing.
- N up to the number of in-connections

**Yield Sign**:
- N up to the number of in-connections

**Light**:
- N protected left turns
- M protected right runs
- S Sensors up to C_in

**Roundabouts** - must yield to left bound traffic. (use average yield constant)
- L lanes per In-connection

#### Model

Each intersection has C_in incoming connections and C_out outgoing connections. at each in-connection, it has L lanes, one flow controller, flow capacity per lane, and current flow 

#### Simulation
Given a intersection configuration IC, and a network flow simulation algorythm, the intersection is modeled and tested against the algorythm to find the average exit time per lane and per lane type. This is checked against a no stop average exit time for a relative effeciency score to be produced. 

### Problem 2:
given a traffic network, where Nodes are the intersections and roads are the edges, how do we determine weak points and what is the MCS (Minimal Change Solution) for those chokepoints.


