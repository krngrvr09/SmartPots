package com.example.krngrvr09.hackathon;

import android.os.Handler;
import android.os.Looper;
import android.os.Message;
import android.util.Log;

import java.io.IOException;
import java.net.DatagramPacket;
import java.net.DatagramSocket;
import java.net.SocketException;

/**
 * Created by krngrvr09 on 14/3/15.
 */
public class MyThread extends Thread {
    Handler mHandler = MainActivity.mHandler;

    private boolean bKeepRunning = true;
    private String lastMessage = "";
    int MAX_UDP_DATAGRAM_LEN = 10;
    int UDP_SERVER_PORT = 10000;
    DatagramSocket socket = null;
    public void run() {
        String message;
        byte[] lmessage = new byte[MAX_UDP_DATAGRAM_LEN];
        DatagramPacket packet = new DatagramPacket(lmessage, lmessage.length);

        try {
            socket = new DatagramSocket(UDP_SERVER_PORT);
            while(bKeepRunning) {
                socket.receive(packet);
                message = new String(lmessage, 0, packet.getLength());
                lastMessage = message;
                //Log.d("message",lastMessage);
                Message msg = Message.obtain();
                msg.obj = lastMessage;
                mHandler.sendMessage(msg);


            }
        } catch (Throwable e) {
            e.printStackTrace();
        }

        if (socket != null) {
            socket.close();
        }
    }

    public void kill() {
        bKeepRunning = false;
    }

    public String getLastMessage() {
        return lastMessage;
    }
}
