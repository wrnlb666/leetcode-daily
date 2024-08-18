class Solution {
    fun nthUglyNumber(n: Int): Int {
        val uglySet = HashSet<Long>()
        uglySet.add(1)

        var curr: Long = 1
        for (i in 0..<n) {
            curr = uglySet.min()
            uglySet.remove(curr)

            uglySet.add(curr * 2)
            uglySet.add(curr * 3)
            uglySet.add(curr * 5)
        }
        return curr.toInt()
    }
}


fun main() {
    val n = 10;
    val res = Solution().nthUglyNumber(n)
    println(res)
}
