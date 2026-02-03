import React, { useMemo } from 'react';

const BarChart = ({ array, comparisons = [], swaps = [], sortedIndices = [] }) => {
    // Determine the max value for scaling height
    const maxValue = useMemo(() => Math.max(...array, 100), [array]);

    return (
        <div className="flex-1 bg-white p-6 rounded-lg shadow-md h-96 flex flex-col justify-end items-center relative overflow-hidden">
            <div className="flex items-end justify-center w-full h-full space-x-1">
                {array.map((value, idx) => {
                    // Determine color based on state
                    let bgColor = 'bg-blue-500'; // Default

                    if (sortedIndices.includes(idx)) {
                        bgColor = 'bg-green-500'; // Sorted
                    } else if (swaps.includes(idx)) {
                        bgColor = 'bg-red-500'; // Just swapped
                    } else if (comparisons.includes(idx)) {
                        bgColor = 'bg-yellow-400'; // Being compared
                    }

                    // Calculate height percentage
                    const height = `${(value / maxValue) * 100}%`;
                    const widthPercent = Math.max(0.5, 100 / array.length - 0.2); // Dynamic width

                    return (
                        <div
                            key={idx}
                            style={{
                                height,
                                width: `${widthPercent}%`
                            }}
                            className={`${bgColor} bar-transition rounded-t-sm shadow-sm opacity-90 hover:opacity-100`}
                            title={`Value: ${value}`}
                        ></div>
                    );
                })}
            </div>
            {array.length === 0 && (
                <div className="absolute inset-0 flex items-center justify-center text-gray-400">
                    No array to visualize
                </div>
            )}
        </div>
    );
};

export default BarChart;
