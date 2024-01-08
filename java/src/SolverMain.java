package src;

public class SolverMain {
	
	public static final int maxAttempts = 10000000;

	public static void main(String[] args) {
		
		SubstitutionSolver solverRandom = new SolverRandom();
		String plainText;
		String cipherText;

		// 1
		plainText = "A";
		cipherText = "X";
		runTest(solverRandom, cipherText, plainText);
		
		// 1
		plainText = "AAAAA";
		cipherText = "XXXXX";
		runTest(solverRandom, cipherText, plainText);

		// 3
		plainText = "ABC";
		cipherText = "XYZ";
		runTest(solverRandom, cipherText, plainText);

		// 4
		plainText = "ABCD";
		cipherText = "WXYZ";
		runTest(solverRandom, cipherText, plainText);

		// 4
		plainText = "ABCD ABCD ABCD";
		cipherText = "WXYZ WXYZ WXYZ";
		runTest(solverRandom, cipherText, plainText);

		// 5
		plainText = "ABCDE";
		cipherText = "VWXYZ";
		runTest(solverRandom, cipherText, plainText);

		// 6
		plainText = "ABCDEF";
		cipherText = "UVWXYZ";
		runTest(solverRandom, cipherText, plainText);

		// 7
		plainText = "ABCDEFG";
		cipherText = "TUVWXYZ";
		runTest(solverRandom, cipherText, plainText);

		// 12
		plainText = "OTTER CREEK MIDDLE SCHOOL";
		cipherText = "ABBCD EDCCF GHDDIC JEKAAL";
		runTest(solverRandom, cipherText, plainText);
	}
	
	private static void runTest(SubstitutionSolver solver, String cipherText, String plainText) {
		System.out.println("Cracking the Code!");
		System.out.println("  plain text  '" + plainText + "'");
		System.out.println("  cipher text '" + cipherText + "'.");
		
		StopWatch timer = new StopWatch();
		timer.start();
		int attemptsNeeded = solver.decipher(cipherText, plainText, SolverMain.maxAttempts);
		timer.stop();
		
		double time = timer.getTimeTakenInSeconds();
		if (attemptsNeeded < SolverMain.maxAttempts) {
			System.out.println("Success!  Attempts: " + attemptsNeeded + "   Time: " + time + " seconds.");	
		} else {
			System.out.println("Failure! :( Gave up after " + attemptsNeeded + " attempts.   Time: " + time + " seconds.");
		}
		System.out.println();
		System.out.println();
	}

}
