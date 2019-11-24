package com.vijithasashwat.myapplication;

import android.content.Intent;
import android.os.Bundle;
import android.support.annotation.NonNull;
import android.support.annotation.Nullable;
import android.support.design.widget.BottomNavigationView;
import android.support.v7.app.AppCompatActivity;
import android.util.Log;
import android.view.MenuItem;
import android.view.View;
import android.widget.AdapterView;
import android.widget.ArrayAdapter;
import android.widget.CheckBox;
import android.widget.ImageButton;
import android.widget.Spinner;
import android.widget.TableLayout;
import android.widget.TableRow;
import android.widget.TextView;
import android.widget.Toast;

import com.google.firebase.database.DataSnapshot;
import com.google.firebase.database.DatabaseError;
import com.google.firebase.database.DatabaseReference;
import com.google.firebase.database.FirebaseDatabase;
import com.google.firebase.database.ValueEventListener;

import org.w3c.dom.Text;

import java.util.ArrayList;
import java.util.List;

public class ActivityOne extends AppCompatActivity {
    FirebaseDatabase firebaseDatabase = FirebaseDatabase.getInstance();
    DatabaseReference mRootReference = firebaseDatabase.getReference();
    DatabaseReference rfirebaseLog = mRootReference.child("log");
    ArrayList<String> yearList = new ArrayList<String>();
    ArrayList<String> monthList = new ArrayList<String>();
    ArrayList<String> dayList = new ArrayList<String>();
    ArrayList<String> timeList = new ArrayList<String>();
    ArrayList<String> actionList = new ArrayList<String>();
    ArrayAdapter<String> adapterYear, adapterMonth, adapterDay,adapterLogTime,adapterLogAction;
    DatabaseReference rfirebaselogMonth;
    DatabaseReference rfirebaselogDay;
    DatabaseReference rfirebaselogTime;
    DatabaseReference rfirebaseLogTimeAction;
    TableLayout logTable;

    @Override
    protected void onCreate(@Nullable Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_one);
        Spinner spinYear = (Spinner)findViewById(R.id.spinnerYear);
        Spinner spinMonth = (Spinner)findViewById(R.id.spinnerMonth);
        Spinner spinDay = (Spinner)findViewById(R.id.spinnerDay);
        logTable = (TableLayout)findViewById(R.id.logTable);
        logTable.setColumnStretchable(0, true);
        logTable.setColumnStretchable(1,true);


        adapterYear = new ArrayAdapter<String>(this, android.R.layout.simple_spinner_item, yearList);
        adapterYear.setDropDownViewResource(android.R.layout.simple_spinner_dropdown_item);
        spinYear.setAdapter(adapterYear);

        adapterMonth = new ArrayAdapter<String>(this, android.R.layout.simple_spinner_item, monthList);
        adapterMonth.setDropDownViewResource(android.R.layout.simple_spinner_dropdown_item);
        spinMonth.setAdapter(adapterMonth);

        adapterDay = new ArrayAdapter<String>(this, android.R.layout.simple_spinner_item, dayList);
        adapterDay.setDropDownViewResource(android.R.layout.simple_spinner_dropdown_item);
        spinDay.setAdapter(adapterDay);

        rfirebaseLog.addValueEventListener(new ValueEventListener() {
            @Override
            public void onDataChange(@NonNull DataSnapshot dataSnapshot) {
                for (DataSnapshot postSnapshot: dataSnapshot.getChildren()) {
//                    Log.e("year",postSnapshot.getKey().toString());
                    yearList.add(postSnapshot.getKey().toString());
                }
                adapterYear.notifyDataSetChanged();
            }

            @Override
            public void onCancelled(@NonNull DatabaseError databaseError) {

            }
        });

        spinYear.setOnItemSelectedListener(new AdapterView.OnItemSelectedListener() {
            @Override
            public void onItemSelected(AdapterView<?> adapterView, View view, int i, long l) {
                rfirebaselogMonth = rfirebaseLog.child(yearList.get(i));
                rfirebaselogMonth.addValueEventListener(new ValueEventListener() {
                    @Override
                    public void onDataChange(@NonNull DataSnapshot dataSnapshot) {
                        for (DataSnapshot postSnapshot: dataSnapshot.getChildren()) {
                            monthList.add(postSnapshot.getKey().toString());
                        }
                        adapterMonth.notifyDataSetChanged();
                    }

                    @Override
                    public void onCancelled(@NonNull DatabaseError databaseError) {

                    }
                });
            }

            @Override
            public void onNothingSelected(AdapterView<?> adapterView) {

            }
        });

        spinMonth.setOnItemSelectedListener(new AdapterView.OnItemSelectedListener() {
            @Override
            public void onItemSelected(AdapterView<?> adapterView, View view, int i, long l) {
                rfirebaselogDay = rfirebaselogMonth.child(monthList.get(i));
                rfirebaselogDay.addValueEventListener(new ValueEventListener() {
                    @Override
                    public void onDataChange(@NonNull DataSnapshot dataSnapshot) {
                        for (DataSnapshot postSnapshot: dataSnapshot.getChildren()) {
                            dayList.add(postSnapshot.getKey().toString());
                        }
                        adapterDay.notifyDataSetChanged();
                    }

                    @Override
                    public void onCancelled(@NonNull DatabaseError databaseError) {

                    }
                });
            }

            @Override
            public void onNothingSelected(AdapterView<?> adapterView) {

            }
        });

        spinDay.setOnItemSelectedListener(new AdapterView.OnItemSelectedListener() {
            @Override
            public void onItemSelected(AdapterView<?> adapterView, View view, int i, long l) {
                rfirebaselogTime = rfirebaselogDay.child(dayList.get(i));
                rfirebaselogTime.addValueEventListener(new ValueEventListener() {
                    @Override
                    public void onDataChange(@NonNull DataSnapshot dataSnapshot) {
                        for (DataSnapshot postSnapshot: dataSnapshot.getChildren()) {
                            timeList.add(postSnapshot.getKey().toString());
                            final TextView logTimeT = (TextView) new TextView(getApplicationContext());
                            logTimeT.setTextSize(18);
                            logTimeT.setText(postSnapshot.getKey().toString());
                            TableRow logTableRow = new TableRow(getApplicationContext());
//                            logTableRow.addView(logTimeT);
//                            logTable.addView(logTableRow);

                            rfirebaseLogTimeAction = rfirebaselogTime.child(postSnapshot.getKey().toString()).child("action");
                            rfirebaseLogTimeAction.addValueEventListener(new ValueEventListener() {
                                @Override
                                public void onDataChange(@NonNull DataSnapshot dataSnapshot) {
                                    actionList.add(dataSnapshot.getValue(String.class));
                                    TextView logStatusT = (TextView) new TextView(getApplicationContext());
                                    logStatusT.setTextSize(18);
                                    logStatusT.setText(dataSnapshot.getValue(String.class));
                                    TableRow logTableRow = new TableRow(getApplicationContext());
                                    logTableRow.addView(logTimeT);
                                    logTableRow.addView(logStatusT);
                                    logTable.addView(logTableRow);
                                }

                                @Override
                                public void onCancelled(@NonNull DatabaseError databaseError) {

                                }
                            });
                        }
                        Log.e("Log time", timeList.toString());

                    }

                    @Override
                    public void onCancelled(@NonNull DatabaseError databaseError) {

                    }
                });

            }

            @Override
            public void onNothingSelected(AdapterView<?> adapterView) {

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

