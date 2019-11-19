package com.vijithasashwat.myapplication;

import android.content.Intent;
import android.os.Bundle;
import android.support.annotation.NonNull;
import android.support.annotation.Nullable;
import android.support.design.widget.BottomNavigationView;
import android.support.v7.app.AppCompatActivity;
import android.view.MenuItem;
import android.widget.CheckBox;
import android.widget.ImageButton;
import android.widget.TableLayout;
import android.widget.TableRow;
import android.widget.TextView;

import com.google.firebase.database.DataSnapshot;
import com.google.firebase.database.DatabaseError;
import com.google.firebase.database.DatabaseReference;
import com.google.firebase.database.FirebaseDatabase;
import com.google.firebase.database.ValueEventListener;

public class ActivityOne extends AppCompatActivity {
    FirebaseDatabase firebaseDatabase = FirebaseDatabase.getInstance();
    DatabaseReference mRootReference = firebaseDatabase.getReference();
    DatabaseReference rfirebaseLog = mRootReference.child("log");

    @Override
    protected void onCreate(@Nullable Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_one);

        rfirebaseLog.addValueEventListener(new ValueEventListener() {
            @Override
            public void onDataChange(@NonNull DataSnapshot dataSnapshot) {
                TableLayout ll = (TableLayout) findViewById(R.id.logTable);
                for (int i = 0; i <2; i++) {

                    TableRow row= new TableRow(this);
                    TableRow.LayoutParams lp = new TableRow.LayoutParams(TableRow.LayoutParams.WRAP_CONTENT);
                    row.setLayoutParams(lp);
                    CheckBox checkBox = new CheckBox(this);
                    TextView qty = new TextView(this);
                    checkBox.setText("hello");
                    qty.setText("10");
                    row.addView(checkBox);
                    row.addView(qty);
                    ll.addView(row,i);
                }

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
                        Intent a = new Intent(ActivityOne.this,home.class);
                        startActivity(a);
                        break;
                    case R.id.navigation_log:
                        break;
                    case R.id.navigation_usage:
                        Intent c = new Intent(ActivityOne.this,ActivityTwo.class);
                        startActivity(c);
                        break;
                }
                return false;
            }
        });
    }


}

