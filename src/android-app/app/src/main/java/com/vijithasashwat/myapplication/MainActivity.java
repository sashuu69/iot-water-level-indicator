package com.vijithasashwat.myapplication;

import android.content.Intent;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;

public class MainActivity extends AppCompatActivity {
    EditText et1,et2;
    Button btn;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        et1=(EditText) findViewById(R.id.edt1);
        et2=(EditText) findViewById(R.id.edt2);
        btn=(Button)findViewById(R.id.btn);
        btn.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                String str1;
                String str2;
                String str3;
                String str4;
                str1 ="uname";
                str2 = "pwd";
                str3=et1.getText().toString();
                str4=et2.getText().toString();
                if(str1.equals(str3))
                {
                    if(str2.equals(str4)) {
                        Intent i = new Intent(MainActivity.this, home.class);
                        startActivity(i);
                    }
                }}
        });

    }
}
