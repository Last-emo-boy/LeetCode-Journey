class Solution:
    def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 初始化前缀和为0
        prefix_sum = 0
        # 初始化虚拟头节点
        dummy = ListNode(0)
        dummy.next = head
        # 初始化哈希表
        prefix = {0: dummy}
        # 遍历链表
        while head:
            # 计算前缀和
            prefix_sum += head.val
            # 如果前缀和已经存在于哈希表中，说明存在连续子序列的和为0
            if prefix_sum in prefix:
                # 获取和为0的连续子序列的前一个节点
                node = prefix[prefix_sum]
                # 保存当前节点的下一个节点
                next_node = node.next
                # 计算前缀和
                sub_sum = prefix_sum + next_node.val
                # 从哈希表中删除和为0的连续子序列
                while sub_sum != prefix_sum:
                    del prefix[sub_sum]
                    next_node = next_node.next
                    sub_sum += next_node.val
                # 删除和为0的连续子序列
                node.next = next_node.next
            else:
                # 如果前缀和不存在于哈希表中，那么将前缀和和当前节点插入到哈希表中
                prefix[prefix_sum] = head
            # 继续下一个节点
            head = head.next
        # 返回结果链表的头节点
        return dummy.next