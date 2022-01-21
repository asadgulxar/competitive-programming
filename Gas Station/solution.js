// Problem Link: https://leetcode.com/problems/gas-station/submissions/
var canCompleteCircuit = function (gas, cost) {
  if (gas.length == cost.length) {
    let startingStation = 0;
    let totalFuel = 0;
    let tank = 0;
    for (let i = 0; i < gas.length; i++) {
      tank = tank + gas[i] - cost[i];
      if (tank < 0) {
        startingStation = i + 1;
        totalFuel = totalFuel + tank;
        tank = 0;
      }
    }

    if (totalFuel + tank < 0) return -1;
    else return startingStation;
  }
  return -1;
};
