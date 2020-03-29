#include <opencv2/opencv.hpp>
#include <iostream>

int main(int argc, char** argv){

  cv::namedWindow("Window", cv::WINDOW_AUTOSIZE);

  cv::VideoCapture cap;
  if (argc==1) {
    cap.open(0); /// if no argument is given take frames from webcam
  } else{
    cap.open(argv[1]); /// if a video file is given read frames from it
  }
  if(!cap.isOpened()) { /// in case of error
    std::cerr <<"Couldn't open capture." << std::endl;
    return -1;
  }


  /// Read and show the first frame
  cv::Mat frame;
  cap>>frame;
  cv::imshow("Window", frame);

  /// Select with mouse a rectangle (r) which we will use to create the region of interest (roi)
  cv::Scalar chosencolor=cv::Scalar(0,0,250);
  cv::Rect2d r=selectROI(frame); ///the function selectROI creates a rectangle (r)

  /// Find r points (coordinates). Rectangle coordinates are: 1) the upper-left point and 2) the distances from it (width and height)
  cv::Point2i rUpLeft(r.x,r.y);
  cv::Point2i rBottRight(r.x+r.width,r.y+r.height); ///To ask for the bottom-right coordinates we must use distances from upper-left point, while to create a new rect we can use the bottom-right point directly


  /// Create template from the roi (to work properly we must copy from roi to Mat)
  cv::Mat roi(frame,r);
  cv::Mat templ;
  roi.copyTo(templ);
  cv::rectangle(frame, r, chosencolor, 1,0 );


  /// Create a sub-roi (first a sub-rectangle) where to apply matchtemplate (all frame is computing-heavy and can cause mismatches if template is little and too common in whole frame)
  cv::Point2i subrectUpLeft(rUpLeft.x-100,rUpLeft.y-50);  ///Change these values to change matching region (also next line)
  cv::Point2i subrectBottRight(rBottRight.x+100,rBottRight.y+150);
  cv::Rect2d subrect(subrectUpLeft,subrectBottRight);
  cv::rectangle( frame, subrect, cv::Scalar::all(255), 2,8,0 );



  cv::imshow("Window", frame);

  cv::waitKey(5000);



  for(;;) {


    cap >> frame;
    if(frame.empty()) break;

    cv::imshow("Template",templ);


    /// Create a subframe from subrect
    /// The (new) sub-frame must be taken from the new frame but using the rectangle from the former frame

    cv::Mat subframe=frame(subrect);
    cv::rectangle( frame, subrect, cv::Scalar::all(250), 1,8,0 );




    cv::Mat ftmp;
    int result_cols =  subframe.cols - templ.cols + 1;
    int result_rows = subframe.rows - templ.rows + 1;
    ftmp.create(result_rows, result_cols, CV_32FC1);
    cv::matchTemplate(subframe, templ,ftmp, 5);
    cv::normalize(ftmp,ftmp,0,1,cv::NORM_MINMAX,-1,cv::Mat());

    /// Localizing the best match with minMaxLoc function
    double minVal; double maxVal; cv::Point minLoc; cv::Point maxLoc;
    cv::Point matchLoc;
    cv::minMaxLoc( ftmp, &minVal, &maxVal, &minLoc, &maxLoc, cv::Mat() );
    matchLoc=maxLoc;


    /// New rectangle calculated adding coordinates from matchLoc (in frmp) to sub-rectangle
    cv::Point2i newTemplRectUpLeft(matchLoc.x+subrectUpLeft.x, matchLoc.y+subrectUpLeft.y);
    cv::Point2i newTemplRectBottRight( cv::Point( matchLoc.x + templ.cols +subrectUpLeft.x, matchLoc.y + templ.rows +subrectUpLeft.y));
    cv::Rect2d newTemplRect(newTemplRectUpLeft, newTemplRectBottRight);
    cv::rectangle( frame, newTemplRect, cv::Scalar::all(0), 2,8,0 );



    /// Create the new template
    cv::Mat templ2;
    cv::Mat roi2(frame,newTemplRect);
    roi2.copyTo(templ2);
    templ=templ2;



    /// Create the new subrect
    cv::Point2i subrect2UpLeft(newTemplRectUpLeft.x-100,newTemplRectUpLeft.y-50);  ///Change these values to change matching region (also next line)
    cv::Point2i subrect2BottRight(newTemplRectBottRight.x+100,newTemplRectBottRight.y+150);
    cv::Rect2d subrect2(subrect2UpLeft,subrect2BottRight);
    cv::rectangle( frame, subrect2, cv::Scalar::all(255), 2,8,0 );

    /// Update the rectangle which originates the subframe
    subrect=subrect2;




    cv::imshow("Window", frame);
    if(cv::waitKey(33)>=0) break;
  }

  return 0;

}
