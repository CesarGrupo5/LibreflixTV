package br.edu.cesarschool.libreflixapp.telas;

import android.annotation.SuppressLint;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.ImageButton;

import androidx.activity.EdgeToEdge;
import androidx.appcompat.app.AppCompatActivity;
import androidx.core.graphics.Insets;
import androidx.core.view.ViewCompat;
import androidx.core.view.WindowInsetsCompat;

import br.edu.cesarschool.libreflixapp.R;

public class MainActivity extends AppCompatActivity {
    boolean menuOpen = true;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        EdgeToEdge.enable(this);
        setContentView(R.layout.activity_main);
        ViewCompat.setOnApplyWindowInsetsListener(findViewById(R.id.main), (v, insets) -> {
            Insets systemBars = insets.getInsets(WindowInsetsCompat.Type.systemBars());
            v.setPadding(systemBars.left, systemBars.top, systemBars.right, systemBars.bottom);
            return insets;
        });

        if(menuOpen) openMenu();
        View menuButton = findViewById(R.id.menuButton);
        menuButton.setOnClickListener(v -> openMenu());
    }

    @SuppressLint("SetTextI18n")
    public void openMenu() {
        View menu = findViewById(R.id.menu);
        ImageButton button = findViewById(R.id.menuButton);

        if(menuOpen) {
            menu.animate().translationX(-menu.getWidth());
            button.animate().translationX(-menu.getWidth());;
            menuOpen = false;
        } else {
            menu.animate().translationX(0);
            button.animate().translationX(0);
            menuOpen = true;
        }
    }
}