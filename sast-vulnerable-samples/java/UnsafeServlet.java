package com.sast.samples;

import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.sql.Connection;
import java.sql.ResultSet;
import java.sql.Statement;

public class UnsafeServlet extends HttpServlet {
    private Connection connection; // Intentionally unused/undefined for SAST demonstration

    @Override
    protected void doGet(HttpServletRequest req, HttpServletResponse resp) throws IOException {
        PrintWriter out = resp.getWriter();

        String user = req.getParameter("user");
        String id = req.getParameter("id");
        String path = req.getParameter("path");
        String cmd = req.getParameter("cmd");

        // SQL Injection (A03:2021 Injection)
        try {
            Statement stmt = connection.createStatement();
            ResultSet rs = stmt.executeQuery("SELECT * FROM users WHERE name = '" + user + "' AND id = " + id);
            while (rs.next()) {
                out.println("User: " + rs.getString("name"));
            }
        } catch (Exception ignored) { }

        // Reflected XSS (A03:2021 Injection / XSS)
        out.println("<html><body>Welcome " + user + "</body></html>");

        // Path Traversal (A01:2021 Broken Access Control)
        try {
            String content = new String(Files.readAllBytes(Paths.get("/var/data/" + path)));
            out.println(content);
        } catch (Exception ignored) { }

        // Command Injection (A03:2021 Injection)
        if (cmd != null) {
            try {
                Process p = Runtime.getRuntime().exec("ping -c 1 " + cmd);
                BufferedReader r = new BufferedReader(new InputStreamReader(p.getInputStream()));
                String line;
                while ((line = r.readLine()) != null) {
                    out.println(line);
                }
            } catch (Exception ignored) { }
        }
    }
}


