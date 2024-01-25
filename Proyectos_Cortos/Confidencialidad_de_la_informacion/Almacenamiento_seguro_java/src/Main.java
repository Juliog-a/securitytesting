import javax.crypto.Cipher;
import javax.crypto.SecretKey;
import javax.crypto.KeyGenerator;

import java.io.FileInputStream;
import java.nio.file.Files;
import java.nio.file.Path;
import java.security.Key;
import java.security.KeyStore;
import java.security.SecureRandom;
import javax.crypto.spec.IvParameterSpec;

public class Main {
    public static void main(String[] args) throws Exception {
       // Configura el almacén de claves
          KeyStore ks = KeyStore.getInstance("JKS");
          char[] password = "clave1".toCharArray(); 
          FileInputStream fis = new FileInputStream("keystore.jks");
          ks.load(fis, password);
          Key privateKey = ks.getKey("clave1", password);

    	
        // Genera un vector de inicialización (IV)
        SecureRandom random = new SecureRandom();
        byte[] iv = new byte[16];
        random.nextBytes(iv);

        Cipher cipher = Cipher.getInstance("AES/CBC/PKCS5Padding");
        cipher.init(Cipher.ENCRYPT_MODE, privateKey, new IvParameterSpec(iv));

        Path imagePath = Path.of("imagen_prueba.jpg");
        byte[] imageBytes = Files.readAllBytes(imagePath);
        byte[] encryptedImageBytes = cipher.doFinal(imageBytes);

        // Guarda el IV junto con los datos cifrados
        byte[] encryptedDataWithIV = new byte[iv.length + encryptedImageBytes.length];
        System.arraycopy(iv, 0, encryptedDataWithIV, 0, iv.length);
        System.arraycopy(encryptedImageBytes, 0, encryptedDataWithIV, iv.length, encryptedImageBytes.length);

        Path encryptedImagePath = Path.of("imagen_cifrada.jpg");
        Files.write(encryptedImagePath, encryptedDataWithIV);

        // Descifra la imagen
        byte[] encryptedData = Files.readAllBytes(encryptedImagePath);

        byte[] ivToUse = new byte[16];
        System.arraycopy(encryptedData, 0, ivToUse, 0, 16);

        cipher.init(Cipher.DECRYPT_MODE, privateKey, new IvParameterSpec(ivToUse));
        byte[] decryptedImageBytes = cipher.doFinal(encryptedData, 16, encryptedData.length - 16);

        Path decryptedImagePath = Path.of("imagen_descifrada.jpg");
        Files.write(decryptedImagePath, decryptedImageBytes);
    }
}


