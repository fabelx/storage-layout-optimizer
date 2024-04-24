// SPDX-License-Identifier: UNLICENSED
pragma solidity ^0.8.0;

contract Mapping {
    mapping(uint8 => uint) public a; // 32                      slot: 0
    mapping(uint => uint8) public b; // 32                      slot: 1
    mapping(bool => uint8) public c; // 32                      slot: 2
    mapping(bool => mapping(bool => uint8)) public d; // 32     slot: 3

//    TOTAL: 4
}