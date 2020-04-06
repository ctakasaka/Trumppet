package main;
import org.python.util.PythonInterpreter;

public class JythonTest {
	// NOT USING JYTHON, OUTDATED
	public static void main(String[] args) {
		System.out.println("Test");
		try(PythonInterpreter python = new PythonInterpreter()){
			python.exec("import sys\nprint(sys.version)");
			python.exec("import tkinter as tk\n"
					  + "window = tk.Tk()\n"
					  + "label = tk.Label(text='test')\n"
					  + "label.pack()\n"
					  + "window.mainloop()\n");
		
		}
	}
}
