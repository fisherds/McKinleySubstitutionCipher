package src;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.Map;
import java.util.Random;

public class SolverLetterFrequencyOnly implements SubstitutionSolver {

	// From
	// https://www3.nd.edu/~busiforc/handouts/cryptography/letterfrequencies.html
	public static final Map<Character, Double> ENGLISH_LETTER_FREQUENCY;
	static {
		ENGLISH_LETTER_FREQUENCY = new HashMap<Character, Double>(26);
		ENGLISH_LETTER_FREQUENCY.put('E', 11.1607); //	E	11.1607	56.88
		ENGLISH_LETTER_FREQUENCY.put('A', 8.4966);  //	A	8.4966	43.31
		ENGLISH_LETTER_FREQUENCY.put('R', 7.5809);  //	R	7.5809	38.64
		ENGLISH_LETTER_FREQUENCY.put('I', 7.5448);  //	I	7.5448	38.45
		ENGLISH_LETTER_FREQUENCY.put('O', 7.1635);	//	O	7.1635	36.51
		ENGLISH_LETTER_FREQUENCY.put('T', 6.9509);	//	T	6.9509	35.43
		ENGLISH_LETTER_FREQUENCY.put('N', 6.6544);	//	N	6.6544	33.92
		ENGLISH_LETTER_FREQUENCY.put('S', 5.7351);	//	S	5.7351	29.23
		ENGLISH_LETTER_FREQUENCY.put('L', 5.4893);	//	L	5.4893	27.98
		ENGLISH_LETTER_FREQUENCY.put('C', 4.5388);	//	C	4.5388	23.13
		ENGLISH_LETTER_FREQUENCY.put('U', 3.6308);	//	U	3.6308	18.51
		ENGLISH_LETTER_FREQUENCY.put('D', 3.3844);	//	D	3.3844	17.25
		ENGLISH_LETTER_FREQUENCY.put('P', 3.1671);	//	P	3.1671	16.14
		ENGLISH_LETTER_FREQUENCY.put('M', 3.0129);	//	M	3.0129	15.36
		ENGLISH_LETTER_FREQUENCY.put('H', 3.0034);	//	H	3.0034	15.31
		ENGLISH_LETTER_FREQUENCY.put('G', 2.4705);	//	G	2.4705	12.59
		ENGLISH_LETTER_FREQUENCY.put('B', 2.0720);	//	B	2.0720	10.56
		ENGLISH_LETTER_FREQUENCY.put('F', 1.8121);	//	F	1.8121	9.24
		ENGLISH_LETTER_FREQUENCY.put('Y', 1.7779);	//	Y	1.7779	9.06
		ENGLISH_LETTER_FREQUENCY.put('W', 1.2899);	//	W	1.2899	6.57
		ENGLISH_LETTER_FREQUENCY.put('K', 1.1016);	//	K	1.1016	5.61
		ENGLISH_LETTER_FREQUENCY.put('V', 1.0074);	//	V	1.0074	5.13
		ENGLISH_LETTER_FREQUENCY.put('X', 0.2902);	//	X	0.2902	1.48
		ENGLISH_LETTER_FREQUENCY.put('Z', 0.2722);	//	Z	0.2722	1.39
		ENGLISH_LETTER_FREQUENCY.put('J', 0.1965);	//	J	0.1965	1.00
		ENGLISH_LETTER_FREQUENCY.put('Q', 0.1962);	//	Q	0.1962	(1)
    }

	public static final String ALPHABET_SORTED_COMMON = "EARIOTNSLCUDPMHGBFYWKVXZJQ";

	Random rand;

	public SolverLetterFrequencyOnly() {
		rand = new Random();
	}

	@Override
	public int decipher(String cipherText, String plainText, int maxAttempts) {
		int counter = 0;
		boolean isSolved = false;
		
		Map<Character, Integer> freqCountMap = new HashMap<Character, Integer>();
		char[] charArray = cipherText.toCharArray();
		for (int k = 0; k < charArray.length; k++) {
			char c = charArray[k];
			if (freqCountMap.containsKey(c)) {
				freqCountMap.put(c, freqCountMap.get(c) + 1);
			} else {
				freqCountMap.put(c, 1);
			}
		}
		int letterTotal = cipherText.length();
		int numUniqueLetters = freqCountMap.keySet().size();
		if (freqCountMap.containsKey(' ')) {
			letterTotal -= freqCountMap.get(' ');
			numUniqueLetters -= 1; // -1 due to spaces
		}
//		System.out.println(cipherText + " has " + numUniqueLetters + " unique letters.");

		while (!isSolved) {
			isSolved = decipherUsingFrequency(cipherText, plainText, freqCountMap, letterTotal);
			counter += 1;

			if (counter >= maxAttempts) {
				System.out.println("SolverLetterFreqOnly Gave up after " + maxAttempts + " attempts.");
				break;
			}
		}
		return counter;
	}

	private boolean decipherUsingFrequency(String cipherText, String plainText, Map<Character, Integer> freqCountMap, int letterTotal) {
		Map<Character, Character> letterMap = new HashMap<>();
		String abc = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
		ArrayList<Character> availableLetters = new ArrayList<Character>();
		for (int k = 0; k < 26; k++) {
			availableLetters.add(abc.charAt(k));
		}

		String workingText = "";
		for (int index = 0; index < cipherText.length(); index++) {
			char cipherLetter = cipherText.charAt(index);
			if (cipherLetter == ' ') {
				workingText += " ";
			} else if (letterMap.containsKey(cipherLetter)) {
				// Subs in the known letter
				workingText += letterMap.get(cipherLetter);
			} else {
				char plainTextLetter = nextLetter(cipherLetter, availableLetters, freqCountMap, letterTotal);
				letterMap.put(cipherLetter, plainTextLetter);
				workingText += plainTextLetter;
			}
		}
		return workingText.equals(plainText);
	}

	private char nextLetter(char cipherLetter, ArrayList<Character> availableLetters, Map<Character, Integer> freqCountMap, int letterTotal) {
		// TODO: Pick the letter based on letter frequencies.
//		return availableLetters.remove(rand.nextInt(availableLetters.size()));
		
		// Instead of just randomly picking a letter select X possible letters and pick from those instead using a weighted average.
		double freq = freqCountMap.get(cipherLetter) * 100.0 / letterTotal; // As a percentage
		int numAvailableLetters = availableLetters.size();
		double[] deltas = new double[numAvailableLetters];
		for (int k = 0; k < availableLetters.size(); k++) {
			char potentialLetter = availableLetters.get(k);
			deltas[k] = Math.abs(freq - ENGLISH_LETTER_FREQUENCY.get(potentialLetter));
		}
		// Rank the letters based on the deltas order. Make a String out of them.
		String mostLikelyLetters = "";
		boolean[] hasBeenUsed = new boolean[availableLetters.size()];
		
		while (mostLikelyLetters.length() < numAvailableLetters) {
			double minDelta = 100;
			int minDeltaIndex = -1;
			char nextLetter = ' ';
			for (int k = 0; k < numAvailableLetters; k++) {
				if (!hasBeenUsed[k] && deltas[k] < minDelta) {
					minDeltaIndex = k;
					nextLetter = availableLetters.get(k);
					minDelta = deltas[k];
				}
			}
			hasBeenUsed[minDeltaIndex] = true;
			mostLikelyLetters += nextLetter;
		}
		//System.out.println(mostLikelyLetters);
		// Weighting the Selection plan.  The first letter has  numAvailableLetters balls in the jar, the last has 1 ball.
		
		StringBuilder weightedMostLikelyLetters = new StringBuilder();
		for (int weight = numAvailableLetters; weight > 0; weight--) {
			for (int k = 0; k < weight; k++) {
				weightedMostLikelyLetters.append(mostLikelyLetters.charAt(numAvailableLetters - weight));
			}
		}
		//System.out.println(weightedMostLikelyLetters);
		char winningLetter = weightedMostLikelyLetters.charAt(rand.nextInt(weightedMostLikelyLetters.length()));
		//System.out.println(winningLetter);
		int indexToRemove = availableLetters.indexOf(winningLetter);
		return availableLetters.remove(indexToRemove);
		
		
	}

}
