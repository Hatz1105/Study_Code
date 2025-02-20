pragma solidity ^0.8.0;

import "forge-std/Test.sol"; // Mengimpor standar testing dari Foundry

contract MyContract is Test {
    uint256 public result;

    function add(uint256 a, uint256 b) public returns (uint256) {
        result = a + b;
        return result;
    }

    // Fungsi pengujian harus dimulai dengan 'test'
    function testAddFunction() public {
        uint256 a = 1;
        uint256 b = 2;
        uint256 expected = 3;

        uint256 actual = add(a, b);
        assertEq(actual, expected); // Memastikan hasilnya sesuai
    }
}
