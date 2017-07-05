import java.io.File;
import java.io.PrintWriter;
import java.util.ArrayList;
import java.util.Formatter;
import java.util.Scanner;

//This is the gift wrap algorithm
//I define a gift wrap class
public class GiftW
{
	//this is a method that returns an arraylist type
	//the way array lists work is you define them as "ArrayList<>" inside the brackets, you put the type of data you're working with, i put Points
	//We use a points class to represent each point 
    public ArrayList<Point> quickwrap(ArrayList<Point> points)
    {
    	//points is the array with all the data we should be analyzing
    	
    	//if data is too small you just return the same data and not waste time running the algorithm
        if (points.size() < 3)
            return (ArrayList)points.clone();
 
        //this is just a variable its pretty useless at this initialization, -1 is just a random number
        int minPoint = -1;
        double minX = Integer.MAX_VALUE;

        //for loop to find the leftmost point in the list, that is we only care about the x value of each point to find the leftmost
        for (int i = 0; i < points.size(); i++)
        {
            if (points.get(i).x < minX)
            {
                minX = points.get(i).x;
                minPoint = i;
                //i gives the position of this leftmost point
            }
        }
        //we save the leftmost point to  pointOnHull because its automatically a point in our convex hull
        Point pointOnHull = points.get(minPoint); 
        Point endpoint;
        int i = 0;
        //p is the array with all our solutions
        ArrayList<Point> p = new ArrayList<Point>();
                
        boolean check = true;
        //we will now iterate through the whole arraylist till we're back at our starting point
        while (check)
        {
        	//adding all our solutions to our arraylist p
        	p.add(pointOnHull);
        	//starting endpoint
        	endpoint = points.get(0);
        	for(int j = 1; j<points.size(); j++)
        	{
        		//looking for our outermost points
            	Point s = points.get(j);
        		if(endpoint == pointOnHull || s.isLeftOfLine(p.get(i), endpoint))
        		{
        			endpoint = points.get(j);
        		}
        	}
        	i++;
        	pointOnHull = endpoint;
        	if(endpoint == p.get(0))
        	{
        		check = false;
        	}
        }
        return p;
    }
    
    public static Scanner x;
    private static Formatter keys;
    public static void main(String args[])
    {
    	//from try to the while loop we're just reading in our data
    	try{
    		x = new Scanner(new File("exercise1.txt"));
    	}
    	catch(Exception e)
    	{
    		System.out.println("could not find file");
    	}
        ArrayList<Point> points = new ArrayList<Point>();
    	int i = 0;
    	while(x.hasNextDouble())
    	{
	    	double x1 = x.nextDouble();
	    	double y = x.nextDouble();
	    	Point e = new Point(x1, y); 
			points.add(i, e);
			i++;
    	}
 
    	//putting our list into algorithm to get solutions
        GiftW qh = new GiftW();
        ArrayList<Point> p = qh.quickwrap(points);
        double t;
        double s;
        try
        {
        	String filename = "pointsFile.txt";
			PrintWriter outputStream = new PrintWriter(filename);
			for(Point g : p)
	        {
	        	t = g.getX();
	        	s = g.getY();
	            outputStream.println(t + " " + s);
	            outputStream.flush();
	        }
			outputStream.close();
        }
        catch(Exception e)
        {
        	e.printStackTrace();
        }

        System.out.println(p);
    }
    
}