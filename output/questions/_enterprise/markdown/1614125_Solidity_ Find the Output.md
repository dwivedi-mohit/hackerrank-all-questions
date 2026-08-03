# Solidity: Find the Output

## Metadata

- **ID:** 1614125
- **Type:** mcq
- **Difficulty:** 1
- **Points:** 5
- **Duration:** N/A minutes
- **Tags:** Solidity, Easy, Blockchain
- **Skills:** Solidity (Basic)

## Summary

This multiple choice question evaluates Solidity, blockchain concepts, and type casting, ideal for junior-level roles. The problem requires determining the output of functions in a Solidity contract that manipulate integer values.

## Problem Statement

What is the output of the functions?

`// SPDX-License-Identifier: MIT
pragma solidity 0.8.19;

contract Challenge {

	function noah() public pure returns (uint32) {
        uint64 x = 500000;
        uint16 y = uint16(x + 65535);
        uint32 z = uint32(y);
        return z;
    }

    function asher() public pure returns (uint16) {
        uint64 x = 500000;
        uint32 y = uint16(x + 65535);
        uint16 z = uint16(y);
        return z;
    }

    function alden() public pure returns (uint32) {
        uint64 x = 500000;
        uint64 y = uint16(x + 65535);
        uint32 z = uint32(y);
        return z;
    }

}
`
```

## Preview

What is the output of the functions?
