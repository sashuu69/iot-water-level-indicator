package com.vijithasashwat.myapplication;

import android.content.Intent;
import android.os.Bundle;
import android.support.annotation.NonNull;
import android.support.design.widget.BottomNavigationView;
import android.support.v7.app.AppCompatActivity;
import android.support.v7.widget.SwitchCompat;
import android.view.MenuItem;
import android.widget.CompoundButton;
import android.widget.Switch;
import android.widget.TextClock;
import android.widget.TextView;
import android.widget.Toast;

import com.google.firebase.database.DatabaseReference;
import com.google.firebase.database.FirebaseDatabase;

import static com.vijithasashwat.myapplication.R.id.pump_status;

public class home extends AppCompatActivity {
    TextView pump_status,tank_status,field_status,garden_status;


    private TextView mTextMessage;
    private DatabaseReference mDatabase;


    private BottomNavigationView.OnNavigationItemSelectedListener mOnNavigationItemSelectedListener
            = new BottomNavigationView.OnNavigationItemSelectedListener() {

        @Override
        public boolean onNavigationItemSelected(@NonNull MenuItem item) {
            switch (item.getItemId()){
                case R.id.navigation_wlevel:
                    break;
                case R.id.navigation_log:
                    Intent a = new Intent(home.this, ActivityOne.class);
                    startActivity(a);
                    break;
                case R.id.navigation_usage:
                    Intent b = new Intent(home.this,ActivityTwo.class);
                    startActivity(b);
                    break;

            }
            return false;
        }
    };

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_home);
        pump_status=(TextView)findViewById(R.id.pump_status);
        tank_status=(TextView)findViewById(R.id.tank_status);
        field_status=(TextView)findViewById(R.id.field_status);
        garden_status=(TextView)findViewById(R.id.garden_status);
        mDatabase = FirebaseDatabase.getInstance().getReference();
        mTextMessage = (TextView) findViewById(R.id.message);
        BottomNavigationView navigation = (BottomNavigationView) findViewById(R.id.navigation);
        navigation.setOnNavigationItemSelectedListener(mOnNavigationItemSelectedListener);

        CompoundButton switchCompat;

        final Switch swi = (Switch) findViewById(R.id.pump_switch);
        swi.setOnCheckedChangeListener(new CompoundButton.OnCheckedChangeListener()
        {
            @Override
            public void onCheckedChanged(CompoundButton buttonView, boolean isChecked) {
                if(swi.isChecked())
                    Toast.makeText(getApplicationContext(), "pump is ON", Toast.LENGTH_SHORT).show();
                else
                    Toast.makeText(getApplicationContext(), "pump is OFF", Toast.LENGTH_SHORT).show();


            }
        });


        }


    }