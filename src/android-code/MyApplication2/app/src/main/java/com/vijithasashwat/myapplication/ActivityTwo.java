package com.vijithasashwat.myapplication;

import android.content.Intent;
import android.os.Bundle;
import android.support.annotation.NonNull;
import android.support.annotation.Nullable;
import android.support.design.widget.BottomNavigationView;
import android.support.v7.app.AppCompatActivity;
import android.view.MenuItem;
import android.widget.TextView;

import com.google.firebase.database.DataSnapshot;
import com.google.firebase.database.DatabaseError;
import com.google.firebase.database.DatabaseReference;
import com.google.firebase.database.FirebaseDatabase;
import com.google.firebase.database.ValueEventListener;

public class ActivityTwo extends AppCompatActivity {
    FirebaseDatabase firebaseDatabase = FirebaseDatabase.getInstance();
    DatabaseReference mRootReference = firebaseDatabase.getReference();
    DatabaseReference rfirebaseDailyUsageFarm = mRootReference.child("daily-usage").child("farm");
    DatabaseReference rfirebaseDailyUsageGarden = mRootReference.child("daily-usage").child("garden");
    DatabaseReference rfirebaseDailyUsagePump = mRootReference.child("daily-usage").child("pump");
    DatabaseReference rfirebaseDailyUsageTank = mRootReference.child("daily-usage").child("tank");
    TextView dailyFarm, dailyGarden, dailyPump, dailyTank;

    @Override
    protected void onCreate(@Nullable Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_two);
        dailyFarm = (TextView) findViewById(R.id.textViewFarmValve);
        dailyGarden = (TextView) findViewById(R.id.textViewGardenValve);
        dailyPump = (TextView) findViewById(R.id.textViewPumpStatus);
        dailyTank = (TextView) findViewById(R.id.textViewTankValve);

        rfirebaseDailyUsageFarm.addValueEventListener(new ValueEventListener() {
            @Override
            public void onDataChange(@NonNull DataSnapshot dataSnapshot) {
                String farmCount = dataSnapshot.getValue(String.class);
                dailyFarm.setText(farmCount);
            }

            @Override
            public void onCancelled(@NonNull DatabaseError databaseError) {

            }
        });

        rfirebaseDailyUsageGarden.addValueEventListener(new ValueEventListener() {
            @Override
            public void onDataChange(@NonNull DataSnapshot dataSnapshot) {
                String gardenCount = dataSnapshot.getValue(String.class);
                dailyGarden.setText(gardenCount);
            }

            @Override
            public void onCancelled(@NonNull DatabaseError databaseError) {

            }
        });

        rfirebaseDailyUsagePump.addValueEventListener(new ValueEventListener() {
            @Override
            public void onDataChange(@NonNull DataSnapshot dataSnapshot) {
                String pumpUsage = dataSnapshot.getValue(String.class);
                dailyPump.setText(pumpUsage);
            }

            @Override
            public void onCancelled(@NonNull DatabaseError databaseError) {

            }
        });

        rfirebaseDailyUsageTank.addValueEventListener(new ValueEventListener() {
            @Override
            public void onDataChange(@NonNull DataSnapshot dataSnapshot) {
                String tankUsage = dataSnapshot.getValue(String.class);
                dailyTank.setText(tankUsage);
            }

            @Override
            public void onCancelled(@NonNull DatabaseError databaseError) {

            }
        });

        BottomNavigationView navigation = (BottomNavigationView) findViewById(R.id.navigation);
        navigation.setOnNavigationItemSelectedListener(new BottomNavigationView.OnNavigationItemSelectedListener() {
            @Override
            public boolean onNavigationItemSelected(@NonNull MenuItem menuItem) {
                switch (menuItem.getItemId()){
                    case R.id.navigation_wlevel:
                        Intent a = new Intent(ActivityTwo.this,home.class);
                        startActivity(a);
                        break;
                    case R.id.navigation_log:
                        Intent b = new Intent(ActivityTwo.this,ActivityOne.class);
                        startActivity(b);
                        break;
                    case R.id.navigation_usage:
                        break;
                }
                return false;
            }
        });
    }


        }


