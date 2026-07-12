class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        HashMap<String, List<String>> anagrams = new HashMap<>();
        
        for (String str : strs) {
            char[] chars = str.toCharArray();
            Arrays.sort(chars);

            String key = new String(chars);
            System.out.println(key);

            if (anagrams.containsKey(key)) {
                anagrams.get(key).add(str);
            } else {
                anagrams.computeIfAbsent(key, k -> new ArrayList<>()).add(str);
            }
        }
        System.out.println(anagrams);


        return new ArrayList<>(anagrams.values());
    }
}
