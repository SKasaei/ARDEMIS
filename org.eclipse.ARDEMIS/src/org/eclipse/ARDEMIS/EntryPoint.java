package org.eclipse.ARDEMIS;

import org.eclipse.epsilon.emc.emf.EmfModel;

import py4j.GatewayServer;

public class EntryPoint {
	private Myepsilon Myepsilon;
	
	public EntryPoint() {
		Myepsilon = new Myepsilon();
	}
	
	public Myepsilon getMyepsilon() {
	        return Myepsilon;
	    }
	
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		  GatewayServer gatewayServer = new GatewayServer(new EntryPoint());
		  gatewayServer.start();
		  System.out.println("Gateway Server Started");
	}

}
