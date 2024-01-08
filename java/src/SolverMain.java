package src;

import java.util.ArrayList;

public class SolverMain {

	public static final int maxAttempts = 1000000;

	public static void main(String[] args) {

		SubstitutionSolver solverRandom = new SolverRandom();
		SubstitutionSolver solverFreqOnly = new SolverLetterFrequencyOnly();
		ArrayList<SubstitutionSolver> solvers = new ArrayList<SubstitutionSolver>();
		solvers.add(solverRandom);
		solvers.add(solverFreqOnly);

		String plainText;
		String key;
		String cipherText;

		// 1
		plainText = "A";
		cipherText = "X";
//		runTest(solverRandom, cipherText, plainText);
		runTests(solvers, cipherText, plainText);

		// 1
		plainText = "AAAAA";
		cipherText = "XXXXX";
//		runTest(solverRandom, cipherText, plainText);
		runTests(solvers, cipherText, plainText);

		// 3
		plainText = "ABC";
		cipherText = "XYZ";
//		runTest(solverRandom, cipherText, plainText);

		runTests(solvers, cipherText, plainText);

		// 4
		plainText = "ABCD";
		cipherText = "WXYZ";
//		runTest(solverRandom, cipherText, plainText);
		runTests(solvers, cipherText, plainText);

		// 4
		plainText = "ABCD ABCD ABCD";
		cipherText = "WXYZ WXYZ WXYZ";
		runTests(solvers, cipherText, plainText);

		// 5
		plainText = "ABCDE";
		cipherText = "VWXYZ";
		runTests(solvers, cipherText, plainText);
		
		// 5 most common
		plainText =  "EARIO EARI EAR EA E";
		cipherText = "ABCDE ABCD ABC AB A";
		runTests(solvers, cipherText, plainText);

		// 6
		plainText = "ABCDEF";
		cipherText = "UVWXYZ";
		runTests(solvers, cipherText, plainText);
		
		// 6 most common
		plainText =  "EARIOT EARIO EARI EAR EA E";
		cipherText = "ABCDEF ABCDE ABCD ABC AB A";
		runTests(solvers, cipherText, plainText);

		// 7
//		plainText = "ABCDEFG";
//		cipherText = "TUVWXYZ";
//		runTest(solverRandom, cipherText, plainText);

		// 12
//		plainText = "OTTER CREEK MIDDLE SCHOOL";
//		cipherText = "ABBCD EDCCF GHDDIC JEKAAL";
//		runTest(solverRandom, cipherText, plainText);

		// 4
		plainText = "OTTER";
		key = CipherDecipherUtils.generateKey(plainText);
		cipherText = CipherDecipherUtils.generateCipherText(plainText, key);
		runTests(solvers, cipherText, plainText);

		// 6
		plainText = "OTTER CREEK";
		key = CipherDecipherUtils.generateKey(plainText);
		cipherText = CipherDecipherUtils.generateCipherText(plainText, key);
		runTests(solvers, cipherText, plainText);

		// 10
//		plainText = "OTTER CREEK MIDDLE";
//		key = CipherDecipherUtils.generateKey(plainText);
//		cipherText = CipherDecipherUtils.generateCipherText(plainText, key);
//		runTests(solvers, cipherText, plainText);

		// 12
//		plainText = "OTTER CREEK MIDDLE SCHOOL";
//		key = CipherDecipherUtils.generateKey(plainText);
//		cipherText = CipherDecipherUtils.generateCipherText(plainText, key);
//		runTests(solvers, cipherText, plainText);

	}

	private static void runTests(ArrayList<SubstitutionSolver> solvers, String cipherText, String plainText) {
		for (SubstitutionSolver solver : solvers) {
			runTest(solver, cipherText, plainText);
		}
		System.out.println();
		System.out.println(" --- ");
		System.out.println();
	}

	private static void runTest(SubstitutionSolver solver, String cipherText, String plainText) {
		System.out.println("Cracking the Code with " + solver.getClass().getName());
		System.out.println("  plain text  '" + plainText + "'");
		System.out.println("  cipher text '" + cipherText + "'  unique letters: " + CipherDecipherUtils.getUniqueLetterCount(cipherText));

		StopWatch timer = new StopWatch();
		timer.start();
		int attemptsNeeded = solver.decipher(cipherText, plainText, SolverMain.maxAttempts);
		timer.stop();

		double time = timer.getTimeTakenInSeconds();
		if (attemptsNeeded < SolverMain.maxAttempts) {
			System.out.println("Success!  Attempts: " + attemptsNeeded + "   Time: " + time + " seconds.");
		} else {
			System.out.println(
					"Failure! :( Gave up after " + attemptsNeeded + " attempts.   Time: " + time + " seconds.");
		}
		System.out.println();
	}

}
