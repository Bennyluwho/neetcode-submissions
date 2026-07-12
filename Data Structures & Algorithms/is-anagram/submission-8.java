class Solution {
    public boolean isAnagram(String s, String t) {
        HashMap<Character, Integer> sCharCount = new HashMap<>();
        HashMap<Character, Integer> tCharCount = new HashMap<>();

        for (char c : s.toCharArray()) {
            if (sCharCount.containsKey(c)) {
                sCharCount.put(c, sCharCount.get(c) + 1);
            } else {
                sCharCount.put(c, 1);
            }
        }

        for (char c : t.toCharArray()) {
            if (tCharCount.containsKey(c)) {
                tCharCount.put(c, tCharCount.get(c) + 1);
            } else {
                tCharCount.put(c, 1);
            }
        }
        return sCharCount.equals(tCharCount);
    }
}
