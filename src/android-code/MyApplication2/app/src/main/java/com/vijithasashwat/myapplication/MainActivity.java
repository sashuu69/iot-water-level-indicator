package com.vijithasashwat.myapplication;

import android.content.Intent;
import android.support.annotation.NonNull;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.Toast;

import com.google.firebase.database.DataSnapshot;
import com.google.firebase.database.DatabaseError;
import com.google.firebase.database.DatabaseReference;
import com.google.firebase.database.FirebaseDatabase;
import com.google.firebase.database.ValueEventListener;

public class MainActivity extends AppCompatActivity {
    EditText et1,et2;
    Button btn;
    FirebaseDatabase firebaseDatabase = FirebaseDatabase.getInstance();
    DatabaseReference mRootReference = firebaseDatabase.getReference();
    DatabaseReference rfirebaseUsername = mRootReference.child("users").child("username");
    DatabaseReference rfirebasePassword = mRootReference.child("users").child("password");
    String firebaseUsername;
    String firebasePassword;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        et1=(EditText) findViewById(R.id.edt1);
        et2=(EditText) findViewById(R.id.edt2);
        btn=(Button)findViewById(R.id.btn);

        rfirebaseUsername.addValueEventListener(new ValueEventListener() {
            @Override
            public void onDataChange(@NonNull DataSnapshot dataSnapshot) {
                firebaseUsername = dataSnapshot.getValue(String.class);
            }

            @Override
            public void onCancelled(@NonNull DatabaseError databaseError) {

            }
        });

        rfirebasePassword.addValueEventListener(new ValueEventListener() {
            @Override
            public void onDataChange(@NonNull DataSnapshot dataSnapshot) {
                firebasePassword = dataSnapshot.getValue(String.class);
            }

            @Override
            public void onCancelled(@NonNull DatabaseError databaseError) {

            }
        });

        btn.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                String str1;
                String str2;
                String str3;
                String str4;
                str1 = firebaseUsername;
                str2 = firebasePassword;
                str3=et1.getText().toString();
                str4=et2.getText().toString();
                if(str1.equals(str3))
                {
                    if(str2.equals(str4)) {
                        Intent i = new Intent(MainActivity.this, home.class);
                        Toast.makeText(MainActivity.this, "Login success", Toast.LENGTH_SHORT).show();
                        startActivity(i);
                    }
                    else {
                        Toast.makeText(MainActivity.this, "Login failed. Wrong username or password.", Toast.LENGTH_SHORT).show();
                    }
                }
                else {
                    Toast.makeText(MainActivity.this, "Login failed. Wrong username or password.", Toast.LENGTH_SHORT).show();
                }
            }
        });

    }
}
