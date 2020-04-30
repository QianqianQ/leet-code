#include "cp.h"
#include <cmath>
#include <iostream>
using namespace std;


double corr(const float* data, int nx, int y1, int y2) 
{ 
  
    double sum_y1 = 0.0, sum_y2 = 0.0, sum_y1y2 = 0.0; 
    double squareSum_y1 = 0.0, squareSum_y2 = 0.0; 
  
    int nb = nx<4?nx:4;
    int na = (nx + nb - 1) / nb;
    int nab = na*nb;
    cout<<"nx: "<<nx<<"nb: "<<nb<<"na: "<<na<<"nab: "<<nab<<endl;
    double tsum_y1[nb];
    double tsum_y2[nb];
    double tsum_y1y2[nb];
    double tsquareSum_y1[nb];
    double tsquareSum_y2[nb];
    for  (int k=0;k<nb;k++){
        tsum_y1[k] = 0;
        tsum_y2[k] = 0;
        tsum_y1y2[k] = 0;
        tsquareSum_y1[k] = 0;
        tsquareSum_y2[k] = 0;
    }
    for (int i = 0; i < na; i++) 
    { 
        cout<<"i "<<i<<endl;
        for  (int k=0;k<nb;k++){
         // sum of row y1
        // cout<<"k: "<<k<<endl;
        // cout<<"i*nb+k: "<< i*nb+k<<endl;
        tsum_y1[k] += (double) data[i*nb+k + y1*nx]; 
  
        // sum of row y2
        tsum_y2[k] += (double) data[i*nb+k + y2*nx]; 
  
        // sum of y1[i] * y2[i]
        tsum_y1y2[k] += (double) data[i*nb+k + y1*nx] * (double) data[i*nb+k + y2*nx]; 
  
        // sum of square of array elements
        tsquareSum_y1[k] += pow((double) data[i*nb+k + y1*nx], 2); 
        tsquareSum_y2[k] += pow((double) data[i*nb+k + y2*nx], 2); 
    }  
    } 

    for(int k=0; k<nb;k++){
            sum_y1 += tsum_y1[k];
            sum_y2 += tsum_y2[k];
            sum_y1y2 += tsum_y1y2[k];
            squareSum_y1 += tsquareSum_y1[k];
            squareSum_y2 += tsquareSum_y2[k];
        }

    cout<<sum_y1<<" "<<sum_y2;
    // calculate correlation coefficient
    double corr = (nx * sum_y1y2 - sum_y1 * sum_y2)  
                  / sqrt((nx * squareSum_y1 - pow(sum_y1, 2))  
                      * (nx * squareSum_y2 - pow(sum_y2, 2))); 
  
    return corr; 
} 


void correlate(int ny, int nx, const float* data, float* result) {    
    for (int i=0;i<ny;i++)
    {
        for (int j=0; j<=i; j++)
        {
            result[i + j*ny] = (float) corr(data, nx, j, i);
        }
    }
}


#include "cp.h"
#include <cmath>

using namespace std;

constexpr float infty = std::numeric_limits<float>::infinity();
double corr(const float* data, int nx, int y1, int y2) 
{ 
  
    double sum_y1 = 0.0, sum_y2 = 0.0, sum_y1y2 = 0.0; 
    double squareSum_y1 = 0.0, squareSum_y2 = 0.0; 
  
    constexpr int nb = 4;
    int na = (nx + nb - 1) / nb;
    int nab = na*nb;
    // input data, padded
    std::vector<double> d(nx*nab, infty);
     for (int j = 0; j < nx; ++j) {
       
    }
    float vv[nb];
     for (int kb = 0; kb < nb; ++kb) {
                vv[kb] = infty;
            }

     for (int ka = 0; ka < na; ++ka) {
                for (int kb = 0; kb < nb; ++kb) {
                    float x = d[nab*i + ka * nb + kb];
                    float y = t[nab*j + ka * nb + kb];
                    float z = x + y;
                    vv[kb] = std::min(vv[kb], z);
                }
            }
    for (int i = 0; i < nx; i++) 
    { 
        // sum of row y1
        sum_y1 += (double) data[i + y1*nx]; 
  
        // sum of row y2
        sum_y2 += (double) data[i + y2*nx]; 
  
        // sum of y1[i] * y2[i]
        sum_y1y2 += (double) data[i + y1*nx] * (double) data[i + y2*nx]; 
  
        // sum of square of array elements
        squareSum_y1 += pow((double) data[i + y1*nx], 2); 
        squareSum_y2 += pow((double) data[i + y2*nx], 2); 
    } 

    // calculate correlation coefficient
    double corr = (nx * sum_y1y2 - sum_y1 * sum_y2)  
                  / sqrt((nx * squareSum_y1 - pow(sum_y1, 2))  
                      * (nx * squareSum_y2 - pow(sum_y2, 2))); 
  
    return corr; 
} 


void correlate(int ny, int nx, const float* data, float* result) {    
    for (int i=0;i<ny;i++)
    {
        for (int j=0; j<=i; j++)
        {
            result[i + j*ny] = (float) corr(data, nx, j, i);
        }
    }
}


#include "cp.h"
#include <cmath>
#include <vector>
#include <iostream>

using namespace std;


double calculate_sum(const float* data,int y, int nx){
    double s = 0;
    for (int i=0;i<nx;i++){
        s += (double) data[i + y*nx];
    } 
    return s;
}
    
double calculate_mean(const float* data,int y, int nx){
    double mean = calculate_sum(data,y, nx) / (double) nx;
    
    return mean;
}

double calculate_dev(const float* data,int y, int nx, double mean){
    double s = 0;
    for (int i = 0; i < nx; i++)
    {
        s += pow(((double) data[i + y*nx]-mean), 2);
    }
    
    return sqrt(s / (double) nx);
}


double calculate_squsum(vector<double> data,int y, int nx){
        double s = 0;
        for (int i=0;i<nx;i++){
            s += pow((double) data[i + y*nx],2);
        } 
        return s;
    }

// double pearson(int n, vector<double> x, double xMean, double xStdDev, vector<double> y, double yMean, double yStdDev) {
//     double sum = 0;
//     for (int i = 0; i < n; i++)
//         sum += (x[i] - xMean) * (y[i] - yMean);
    
//     return sum / (n * xStdDev * yStdDev);
// }
double pearson(const float* data, int nx, int y, double xMean, double xStdDev, vector<double> y, double yMean, double yStdDev) {
    double sum = 0;
    for (int i = 0; i < nx; i++)
        sum += (data[i] - xMean) * (y[i] - yMean);
    
    return sum / (n * xStdDev * yStdDev);
}
  
void correlate(int ny, int nx, const float* data, float* result) {   

    std::vector<double> normalized_data(nx*ny);

    for (int i=0;i<ny;i++){
        double mean = calculate_mean(data,i,nx);
        // cout<<mean;
        for(int j=0;j<nx;j++){
            // normalized_data[j + i*nx] = (double) data[j + i*nx] - mean;
            normalized_data[j + i*nx] = ((double) data[j + i*nx] - mean);
            cout<<"j+i*nx: "<<j+i*nx<<" origin: "<<data[j + i*nx]<<endl;

            cout<<"j+i*nx: "<<j+i*nx<<" meaned: "<<normalized_data[j + i*nx]<<endl;
        }
    }
    for (int i=0;i<ny;i++){
        
        // double s = 0;
        // for(int j=0; j<nx;j++){
        //     s += pow(normalized_data[j + i*nx],2);
        // }
        double s = calculate_squsum(normalized_data, i, nx);
        cout<<"s: "<<sqrt(s)<<endl;
        for(int j=0;j<nx;j++){
            // normalized_data[j + i*nx] = (double) data[j + i*nx] - mean;
            normalized_data[j + i*nx] = (normalized_data[j + i*nx]/sqrt(s));
            cout<<"j+i*nx: "<<j+i*nx<<" normalized: "<<normalized_data[j + i*nx];
        }
    }
    
    // for (int i=0;i<ny;i++)
    // {
         
    //     double mean = calculate_mean(data, i, nx);
    //     double dev =  calculate_dev(data,i,nx,mean);
    //     double squsum = calculate_squsum(data,i,nx,mean);
    //     cout<<"y: "<<i<<" mean: "<<mean<<" dev: "<<dev<<" squsum: "<<squsum<<endl;
        
    //     for (int j=0; j<nx; j++)
    //     {
            
    //         double r = ((double)data[j+i*nx]-mean)/(squsum);
    //         normalized_data.push_back(r);
    //         cout<<"j+i*nx: "<<j+i*nx<<" origin: "<<data[j+i*nx]<<" normalized: "<<r;
    //     }
    // }

     for (int i=0; i<ny; i++){
       for(int j=0;j<ny;j++){
           result[i+j*ny] = 0;                                                                  
       }
   }

   for (int i=0; i<ny; i++){
       for(int j=0;j<ny;j++){
           for (int k=0;k<nx;k++){
               result[i + j*ny] += normalized_data[k + i*nx]*normalized_data[k + j*nx];
           }                                                                      
       }
   }
}