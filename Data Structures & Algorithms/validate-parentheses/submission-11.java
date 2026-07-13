class Solution {
    public boolean isValid(String s) {

        HashMap<Character, Character> valid = new HashMap<>();
        Deque<Character> stack = new ArrayDeque<>();

        valid.put('}', '{');
        valid.put(']', '[');
        valid.put(')', '(');

        for (char c : s.toCharArray()) {
            if (!valid.containsKey(c)) {
                stack.push(c);
            } else if (!stack.isEmpty()){
                if (stack.pop() != valid.get(c)) {
                    return false;
                }
            } else {
                return false;
            }
        }

        return stack.isEmpty();
    }
}
