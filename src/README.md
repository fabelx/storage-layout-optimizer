# Storage Layout Optimizer

___
> [!IMPORTANT]
> ## Currently, in development
___

## About
`sl_optimizer` is a Python library designed to optimize the storage layout for [Solidity](https://soliditylang.org/) smart contracts.
Efficient storage layout can reduce the number of storage slots needed, leading to lower gas costs for both storage
and computational operations. It's important to align variables to these slots
efficiently to avoid wasted space and save some money.

___

## Usage
```python
# import the StorageLayout class
from sl_optimizer import StorageLayout


def main():
    # specify the filepath that contains the smart contract storage layout
    sl = StorageLayout(filepath='SomeContract_storage.json')
    # print the contact name
    print(sl.contract_name)
    # print the current number of allocated slots
    print(sl.number_of_slots)
    # run optimization, returns OptimizedStorageLayout
    osl = sl.optimize()
    # save an optimized version of the storage layout to default file
    # file: optimized_storage_layout.json
    osl.save(force=True)
    # print the current number of allocated slots for
    # an optimized version of the smart contract storage layout
    print(osl.number_of_slots)


if __name__ == '__main__':
    main()
```

___

## License
`sl_optimizer` is released under the MIT License.
See the [LICENSE](../LICENSE.txt) file for license information.
