import java.util.Stack;

/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
class Solution {
    public ListNode reverseList(ListNode head) {
        if (head == null) {
            return null;
        }
        Stack<ListNode> stack = new Stack<ListNode>();
        while (head != null) {
            stack.push(head);
            head = head.next;
        }
        System.out.println("xxxxx " + stack.size());
        ListNode ans = stack.peek();
        head = stack.pop();
        while (!stack.empty()) {
            head.next = stack.pop();
            System.out.println("ssssss " + head.val);
            head = head.next;
        }
        head.next = null;
        return ans;
    }

    public static void main(String[] args) {
        ListNode head = new ListNode(1);
        head.next = new ListNode(2);
        head.next.next = new ListNode(3);
        head.next.next.next = new ListNode(4);
        head.next.next.next.next = new ListNode(5);

        Solution solution = new Solution();
        ListNode reverse = solution.reverseList(head);
        while (reverse != null) {
            // System.out.println(reverse.val);
            reverse = reverse.next;
        }
    }
}

class ListNode {
    int val;

    ListNode next;

    ListNode(int x) {
        val = x;
    }
}
