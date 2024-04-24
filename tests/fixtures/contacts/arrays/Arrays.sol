// SPDX-License-Identifier: UNLICENSED
pragma solidity ^0.8.0;

contract Arrays {
    uint8[2] public a;  // 32               slot: 0
    uint[32] public b;  // 32 * 32 (1024)   slots: 1-32
    uint8[] public c;  // 32                slot: 33
    bytes[] public d;   // 32               slot: 34
    bytes[2] public f; // 32 * 2 (64)       slot: 35-36
    string[] public e; // 32                slot: 37

//    TOTAL: 38 slots

}
