package DataStructure;

public class RemoveNthNode {
    public static class ListNode {
        int val;
        ListNode next;
        ListNode() {}
        ListNode(int val) { this.val = val; }
        ListNode(int val, ListNode next) { this.val = val; this.next = next; }
     }

    public ListNode removeNthFromEnd(ListNode head, int n) {
        ListNode counter = new ListNode(0, head);
        int size = 0;

        while (counter.next != null) {
            size++;
            counter = counter.next;
        }

        // base case
        if (size == 1) return null;
        if (size + 1 - n == 1) return head.next;

        ListNode curr = new ListNode(-1, head);
        for (int i = 1; i < (size + 1) - n; i++) {
            curr = curr.next;
        }
        curr.next = curr.next.next;
        return head;
    }
}
