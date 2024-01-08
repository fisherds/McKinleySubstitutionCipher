package src;

import static org.junit.jupiter.api.Assertions.*;

import org.junit.jupiter.api.Test;

class CipherDecipherUtilsTest {

	@Test
	void testFilterPlainText() {
		assertEquals("HELLO WORLD", CipherDecipherUtils.filterPlainText("Hello, World!"));
	}

	@Test
	void testGenerateKey() {
		assertEquals("EOTRCDLKMISH", CipherDecipherUtils.generateKey("OTTER CREEK MIDDLE SCHOOL"));
	}

	@Test
	void testGenerateCipherText() {
		assertEquals("BCCAD EDAAH IJFFGA KELBBG", CipherDecipherUtils.generateCipherText("OTTER CREEK MIDDLE SCHOOL", "EOTRCDLKMISH"));
	}

	@Test
	void testGetPlainText() {
		assertEquals("OTTER CREEK MIDDLE SCHOOL", CipherDecipherUtils.getPlainText("BCCAD EDAAH IJFFGA KELBBG", "EOTRCDLKMISH"));
	}

}
