class Solution {
    fun minSteps(n: Int): Int {
        var n: Int = n
        var res: Int = 0
        for (d in 2..n) {
            while (n % d == 0) {
                res += d
                n /= d
            }
        }
        return res
    }
}


fun main() {
    val n: Int = 3
    val res: Int = Solution().minSteps(n)
    println(res)
}
