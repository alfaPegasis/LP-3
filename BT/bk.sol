pragma solidity ^0.8.0;

contract Bank {
    constructor() {
        
    }
    mapping (address => uint) private balances;

    function getBalance() public view returns (uint) {
        return balances[msg.sender]; 
    }
    function deposit(uint amount) public payable{
        balances[msg.sender] += amount;
    }
    function withdraw(uint amount) public payable{
        balances[msg.sender] -= amount;
    }
}