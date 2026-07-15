class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        List<List<String>> res = new ArrayList<>();
        Map<String, List<String>> anagrams = new HashMap<>();
        
        for (String s : strs) {
            char[] chars = s.toCharArray();
            Arrays.sort(chars);
            String sorted = new String(chars);
            
            if (!anagrams.containsKey(sorted)) {
                anagrams.put(sorted, new ArrayList<>());
                anagrams.get(sorted).add(s);
            } else {
                anagrams.get(sorted).add(s);
            }
        }


        return new ArrayList<>(anagrams.values());
    }
}
