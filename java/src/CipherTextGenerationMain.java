package src;

public class CipherTextGenerationMain {

	public static void main(String[] args) {
		String message = "Display and Safety Committee Mission "
				+ "The mission of this committee is to ensure that all competitors qualify for competition according to the "
				+ "rules established in conjunction with the Scientific Review Committee and Society for Science. "
				+ "The HSEF Display & Safety inspection process can be initiated only when all items are present at the "
				+ "display. The Display & Safety Committee will offer guidance on Display & Safety issues for projects "
				+ "approved by the SRC to compete in HSEF. Occasionally, the HSEF Display & Safety Committee may "
				+ "require students to make revisions to conform to Display & Safety regulations. Persistent issues will be "
				+ "directed to a committee of individuals which may include SEFI personnel, Display & Safety (D&S) "
				+ "and/or Scientific Review Committee (SRC) executive committee members. "
				+ "The following regulations must be adhered to when a student exhibits a project at HSEF. All projects "
				+ "must adhere to the Display & Safety requirements of the affiliated fair(s) in which they compete. "
				+ "Knowledge of these requirements is the responsibility of the Finalist, Adult Sponsor, and Fair Director.";
		message = CipherDecipherUtils.filterPlainText(message);
		String key = CipherDecipherUtils.generateKey(message);
		System.out.println(CipherDecipherUtils.generateCipherText(message, key));
	}

}
