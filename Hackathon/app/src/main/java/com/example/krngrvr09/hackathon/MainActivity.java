package com.example.krngrvr09.hackathon;

import android.content.Intent;
import android.graphics.Typeface;
import android.os.Handler;
import android.os.Looper;
import android.os.Message;
import android.support.v7.app.ActionBarActivity;
import android.os.Bundle;
import android.util.Log;
import android.view.Menu;
import android.view.MenuItem;
import android.view.View;
import android.widget.Button;
import android.widget.TextView;


public class MainActivity extends ActionBarActivity {
    public static Handler mHandler;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        final Button start = (Button) findViewById(R.id.start);
        final TextView plantName = (TextView) findViewById(R.id.plantName);
        final TextView does_doesnt = (TextView) findViewById(R.id.does_doesnt);
        final TextView survival = (TextView) findViewById(R.id.survival);
        Typeface typeFace= Typeface.createFromAsset(getAssets(), "Raleway-ExtraLight.ttf");
        plantName.setTypeface(typeFace);
        does_doesnt.setTypeface(typeFace);
        survival.setTypeface(typeFace);
        start.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                plantName.setVisibility(View.VISIBLE);
                does_doesnt.setVisibility(View.VISIBLE);
                survival.setVisibility(View.VISIBLE);
                start.setVisibility(View.INVISIBLE);
                MyThread mThread = new MyThread();
                mThread.start();
            }
        });
        mHandler = new Handler(){
            public void handleMessage(Message msg){
                Log.d("message here", String.valueOf(msg.obj));
                if(msg.obj.equals("-1")){
                    does_doesnt.setText("doesn't need");
                }
                if(msg.obj.equals("-2")){
                    does_doesnt.setText("doesn't need");

                }
                if(msg.obj.equals("+1")){
                    does_doesnt.setText("needs");

                }
                if(msg.obj.equals("+2")){
                    does_doesnt.setText("needs");

                }


            }
        };




    }


    @Override
    public boolean onCreateOptionsMenu(Menu menu) {
        // Inflate the menu; this adds items to the action bar if it is present.
        getMenuInflater().inflate(R.menu.menu_main, menu);
        return true;
    }

    @Override
    public boolean onOptionsItemSelected(MenuItem item) {
        // Handle action bar item clicks here. The action bar will
        // automatically handle clicks on the Home/Up button, so long
        // as you specify a parent activity in AndroidManifest.xml.
        int id = item.getItemId();

        //noinspection SimplifiableIfStatement
        if (id == R.id.action_settings) {
            return true;
        }

        return super.onOptionsItemSelected(item);
    }
}
