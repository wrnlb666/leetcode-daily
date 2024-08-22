import java.math.BigInteger


class Solution {
    fun findComplement(num: Int): Int {
        val bitLength: Int = BigInteger.valueOf(num.toLong()).bitLength()
        return num.xor(1.shl(bitLength) - 1)
    }
}


fun main() {
    val num: Int = 5
    val res: Int = Solution().findComplement(num)
    println(res)
}

