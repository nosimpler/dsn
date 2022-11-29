# dsn

Analysis of dynamical systems on networks of ordinary differential equations. This is a very unfinished project!

Differential equations must be written symbolically using SymPy. dsn currently supports computation of parametric conditions for synchronization (see Pham and Slotine, 2009) and cosynchronization (see Law, 2014 thesis) using Gershgorin discs on projections of the symbolic Jacobian.

dsn now also supports computation of the flow curvature manifold (Ginoux, 2009). 

TODO: implement Cardon-Crochemore to find minimum base graphs.

TODO: Implement Cassini ovals for better parametric constraints

TODO: Use flow-curvature to obtain more dynamical properties (center manifolds etc.)