package src;

import java.util.HashMap;
import java.util.Map;

public class CipherDecipherUtils {
    private static final String ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
	
	public static String filterPlainText(String rawText) {
        StringBuilder plainText = new StringBuilder();
        for (char c : rawText.toCharArray()) {
        	if (Character.isAlphabetic(c) || c == ' ') {
        		plainText.append(c);        		
        	}
        }
        return plainText.toString().trim().toUpperCase();
	}
	
	public static String generateKey(String plainText) {
		Map<Character, Integer> freqCountMap = new HashMap<Character, Integer>();
		Map<Character, Integer> firstOccuranceMap = new HashMap<Character, Integer>();
		char[] charArray = plainText.toCharArray(); 
		for (int k = 0; k < charArray.length; k++) {
			char c = charArray[k];
        	if (firstOccuranceMap.containsKey(c)) {
        		// Already exist
        		freqCountMap.put(c, freqCountMap.get(c) + 1);
        	} else {
        		firstOccuranceMap.put(c, k);
        		freqCountMap.put(c, 1);
        	}
        }
		
		String key = "";
		freqCountMap.remove(' ');  // remove space
		while (!freqCountMap.isEmpty()) {
			key += getNextLetter(freqCountMap, firstOccuranceMap);
		}
		return key;
	}

	private static char getNextLetter(Map<Character, Integer> freqCountMap, Map<Character, Integer> firstOccuranceMap) {
		char maxChar = ' ';
		int maxCount = 0;
		for (char c : freqCountMap.keySet()) {
			if ((freqCountMap.get(c) > maxCount) || (freqCountMap.get(c) == maxCount && firstOccuranceMap.get(c) < firstOccuranceMap.get(maxChar))) {
				maxChar = c;
				maxCount = freqCountMap.get(c);
			} 
		}
		freqCountMap.remove(maxChar);  // remove the item from the freq map.
		return maxChar;
	}
	
	public static String generateCipherText(String plainText, String key) {
        StringBuilder cipherText = new StringBuilder();
        for (char c : plainText.toCharArray()) {
        	if (c == ' ') {
                cipherText.append(' ');        		
        	} else {
                int index = key.indexOf(c);
                cipherText.append(ALPHABET.charAt(index));
        	}
        }
        return cipherText.toString();
	}
	
	public static String getPlainText(String cipherText, String key) {
        StringBuilder plainText = new StringBuilder();
        for (char c : cipherText.toCharArray()) {
        	if (c == ' ') {
        		plainText.append(' ');        		
        	} else {
                int index = ALPHABET.indexOf(c);
                plainText.append(key.charAt(index));
        	}
        }
        return plainText.toString();
	}
}
