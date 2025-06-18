// mobile_vulns_demo.java
// Exemple d'activités Android avec des vulnérabilités mobiles courantes
// À utiliser uniquement à des fins pédagogiques ou de test SAST/CI

package com.example.mobilevulnsdemo;

import android.app.Activity;
import android.content.SharedPreferences;
import android.os.Bundle;
import android.util.Base64;
import android.util.Log;
import android.widget.EditText;
import java.io.FileOutputStream;
import java.io.IOException;
import java.security.MessageDigest;
import javax.crypto.Cipher;
import javax.crypto.spec.SecretKeySpec;

public class MainActivity extends Activity {
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        // setContentView(R.layout.activity_main); // Layout non nécessaire pour la démo

        // 1. Stockage de données sensibles en clair (SharedPreferences)
        SharedPreferences prefs = getSharedPreferences("my_prefs", MODE_PRIVATE);
        prefs.edit().putString("password", "SuperSecret123").apply();

        // 2. Utilisation d'un algorithme de chiffrement faible (MD5)
        String hash = md5("sensitive_data");
        Log.d("VULN", "MD5 hash: " + hash);

        // 3. Utilisation d'une clé codée en dur
        String encrypted = encryptWithHardcodedKey("secret message");
        Log.d("VULN", "Encrypted: " + encrypted);

        // 4. Écriture de données dans un fichier accessible à tous
        try {
            FileOutputStream fos = openFileOutput("public.txt", MODE_WORLD_READABLE);
            fos.write("data publique".getBytes());
            fos.close();
        } catch (IOException e) {
            e.printStackTrace();
        }

        // 5. Logging de données sensibles
        Log.d("VULN", "Mot de passe utilisateur: SuperSecret123");
    }

    // Vulnérabilité : MD5
    private String md5(String s) {
        try {
            MessageDigest digest = MessageDigest.getInstance("MD5");
            digest.update(s.getBytes());
            byte[] messageDigest = digest.digest();
            StringBuilder hexString = new StringBuilder();
            for (byte b : messageDigest) {
                String h = Integer.toHexString(0xFF & b);
                while (h.length() < 2)
                    h = "0" + h;
                hexString.append(h);
            }
            return hexString.toString();
        } catch (Exception e) {
            return "";
        }
    }

    // Vulnérabilité : clé codée en dur
    private String encryptWithHardcodedKey(String data) {
        try {
            String key = "1234567890123456"; // Clé codée en dur
            SecretKeySpec secretKey = new SecretKeySpec(key.getBytes(), "AES");
            Cipher cipher = Cipher.getInstance("AES");
            cipher.init(Cipher.ENCRYPT_MODE, secretKey);
            byte[] encrypted = cipher.doFinal(data.getBytes());
            return Base64.encodeToString(encrypted, Base64.DEFAULT);
        } catch (Exception e) {
            return null;
        }
    }
} 
