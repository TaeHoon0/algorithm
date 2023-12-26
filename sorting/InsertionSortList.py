class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        # 정렬된 부분 리스트를 첫 번째 노드로 초기화합니다.
        sorted_head = ListNode(0)
        sorted_head.next = head
        sorted_tail = head

        # 첫 번째 노드는 이미 정렬되어 있으므로 두 번째 노드부터 시작합니다.
        curr = head.next

        while curr:
            # 만약 현재 노드가 정렬된 리스트의 끝보다 크다면,
            # 이미 올바른 위치에 있으므로 다음 노드로 이동합니다.
            if curr.val >= sorted_tail.val:
                sorted_tail = curr
                curr = curr.next
            else:
                # 현재 노드를 리스트에서 제거합니다.
                sorted_tail.next = curr.next

                # 정렬된 리스트에 현재 노드를 삽입할 위치를 찾습니다.
                insert_pos = sorted_head
                while insert_pos.next.val < curr.val:
                    insert_pos = insert_pos.next

                # 현재 노드를 정렬된 리스트에 삽입합니다.
                curr.next = insert_pos.next
                insert_pos.next = curr

                # 정렬되지 않은 부분 리스트에서 다음 노드로 이동합니다.
                curr = sorted_tail.next

        return sorted_head.next