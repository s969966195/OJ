class Solution {
    public ListNode deleteDuplicates(ListNode head) {

        if (head == null || head.next == null) {
            return head;
        }

        ListNode cur = head;
        ListNode next = cur.next;
        while (cur.next != null) {
            if (cur.val == next.val) {
                cur.next = next.next;
                next = cur.next;
                continue;
            }
            cur = cur.next;
            next = cur.next;
        }
        return head;

    }


}
