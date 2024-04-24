// SPDX-License-Identifier: UNLICENSED
pragma solidity ^0.8.0;

contract Enums {
    // enum
	enum vEnum {
        Pending,
        Shipped,
        Accepted,
        Rejected,
        Canceled
	}

	vEnum public status = vEnum.Canceled; // 1      slot: 0
    vEnum[55] public statuses; // 55                slot: 1-2
    vEnum public default_status; // 1               slot: 3

//    TOTAL: 4
}