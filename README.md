# Prisoners Riddle
Project of calculating the chances of winning all prisoners depending on their strategy.

The director of a prison offers 100 death row prisoners, who are numbered from 1 to 100, a last chance. A room contains a cupboard with 100 drawers. The director randomly puts one prisoner's number in each closed drawer. The prisoners enter the room, one after another. Each prisoner may open and look into 50 drawers in any order. The drawers are closed again afterwards. If, during this search, every prisoner finds their number in one of the drawers, all prisoners are pardoned. If just one prisoner does not find their number, all prisoners die. Before the first prisoner enters the room, the prisoners may discuss strategy — but may not communicate once the first prisoner enters to look in the drawers. What is the prisoners' best strategy?

## Simulation results

### Random strategy
- Pick any 50 random boxes. 
- Chance of prisoners to win game is ~0%.

### Loop strategy 
- Pick box with prisoner assigned number and then pick box with number founded inside in previuos box and repeat 49 times.
- Chance of prisoners to win game is ~33%.
  
