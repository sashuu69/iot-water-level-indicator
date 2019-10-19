package com.vijithasashwat.waterlevelindicator;

import android.content.Intent;
import android.os.Bundle;
import android.support.annotation.NonNull;
import android.support.design.widget.BottomNavigationView;
import android.support.v7.app.AppCompatActivity;
import android.view.MenuItem;
import android.widget.TextView;

public class MainActivity extends AppCompatActivity {

    private TextView mTextMessage;



    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        mTextMessage = (TextView) findViewById(R.id.message);
        BottomNavigationView navigation = (BottomNavigationView) findViewById(R.id.navigation);
        navigation.setOnNavigationItemSelectedListener(new BottomNavigationView.OnNavigationItemSelectedListener() {
            @Override
            public boolean onNavigationItemSelected(@NonNull MenuItem menuItem) {
                switch (menuItem.getItemId()){
                    case R.id.navigation_wlevel:
                        break;
                    case R.id.navigation_log:
                        Intent a = new Intent(MainActivity.this, ActivityOne.class);
                        startActivity(a);
                        break;
                    case R.id.navigation_usage:
                        Intent b = new Intent(MainActivity.this,ActivityTwo.class);
                        startActivity(b);
                        break;
                }
                return false;
            }
        });
    }

}


