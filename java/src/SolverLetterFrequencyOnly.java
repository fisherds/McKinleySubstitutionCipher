package src;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.Map;
import java.util.Random;

public class SolverLetterFrequencyOnly implements SubstitutionSolver {

	Random rand;

	public SolverLetterFrequencyOnly() {
		rand = new Random();
	}

	@Override
	public int decipher(String cipherText, String plainText, int maxAttempts) {
		int counter = 0;		
		boolean isSolved = false;
		while (!isSolved) {
			isSolved = decipherRandomly(cipherText, plainText); 
			counter += 1;
			
			if (counter >= maxAttempts) {
				System.out.println("SolverRandom Gave up after " + maxAttempts + " attempts.");
				break;
			}
		}
		return counter;
	}

	private boolean decipherRandomly(String cipherText, String plainText) {
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
				char plainTextLetter = nextLetter(availableLetters);
				letterMap.put(cipherLetter, plainTextLetter);
				workingText += plainTextLetter;
			}			
		}		
		return workingText.equals(plainText);
	}
	
	private char nextLetter(ArrayList<Character> availableLetters) {
		// TODO: Pick the letter based on letter frequencies.
		return availableLetters.remove(rand.nextInt(availableLetters.size()));
	}

}
