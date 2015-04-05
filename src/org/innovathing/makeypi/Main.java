package org.innovathing.makeypi;

import java.util.logging.Logger;
import java.util.logging.Level;

import org.jnativehook.GlobalScreen;
import org.jnativehook.NativeHookException;
import org.jnativehook.keyboard.NativeKeyEvent;
import org.jnativehook.keyboard.NativeKeyListener;

public class Main implements NativeKeyListener {

    public void nativeKeyPressed(NativeKeyEvent e)
    {
        System.out.println("Key pressed : " + NativeKeyEvent.getKeyText(e.getKeyCode()));

        if(e.getKeyCode() == NativeKeyEvent.VC_ESCAPE)
        {
            try {
                GlobalScreen.unregisterNativeHook();
            } catch (NativeHookException e1) {
                e1.printStackTrace();
            }
        }

    }

    public void nativeKeyReleased(NativeKeyEvent e)
    {
        System.out.println("Key released : " + NativeKeyEvent.getKeyText(e.getKeyCode()));
    }

    public void nativeKeyTyped(NativeKeyEvent e)
    {
    }

    public static void main(String[] args) {
        try
        {
            GlobalScreen.registerNativeHook();
        } catch (NativeHookException e)
        {
            System.out.println("There was a problem registering the native hook ...");
            System.out.println(e.getMessage());
            System.exit(-1);
        }

        Logger logger = Logger.getLogger(GlobalScreen.class.getPackage().getName());
        logger.setLevel(Level.OFF);
        GlobalScreen.addNativeKeyListener(new Main());

    }
}
