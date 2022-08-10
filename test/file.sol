pragma solidity ^0.4.19;

contract algorithm {
    // addition
    function Add(uint a, uint b) public pure returns(uint) {
        uint r = a + b;
        return r;
    }

    // reduce
    function Reduce(uint a, uint b) public pure returns(uint) {
        uint r = a-b;
        return r;
    }

    // multiple
    function Multiple(uint a, uint b) public pure returns(uint) {
        uint r = a * b;
        return r;
    }

    // divide
    function Divide(uint a, uint b) public pure returns(uint) {
        uint r = a/b;
        return r;
    }

    // pow
    function Pow(uint a, uint b) public pure returns(uint) {
        uint r = a ** b;
        return r;
    }
}


