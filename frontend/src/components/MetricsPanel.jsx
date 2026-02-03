import React, { useMemo } from 'react';

const MetricsPanel = ({ metrics, complexity, algorithm }) => {

    // Format algorithm name for display
    const algoDisplay = algorithm.charAt(0).toUpperCase() + algorithm.slice(1) + " Sort";

    return (
        <div className="bg-white p-6 rounded-lg shadow-md w-full md:w-80 flex-shrink-0">
            <h3 className="text-xl font-bold text-gray-800 mb-4 border-b pb-2">Analytics</h3>

            <div className="space-y-4">
                <div>
                    <p className="text-sm text-gray-500">Algorithm</p>
                    <p className="font-semibold text-lg text-blue-600">{algoDisplay}</p>
                </div>

                <div className="grid grid-cols-2 gap-4">
                    <div className="bg-gray-50 p-3 rounded-md">
                        <p className="text-xs text-gray-500">Comparisons</p>
                        <p className="font-mono text-lg font-bold text-gray-800">{metrics.comparisons}</p>
                    </div>
                    <div className="bg-gray-50 p-3 rounded-md">
                        <p className="text-xs text-gray-500">Swaps</p>
                        <p className="font-mono text-lg font-bold text-gray-800">{metrics.swaps}</p>
                    </div>
                </div>

                <div className="bg-blue-50 p-3 rounded-md border border-blue-100">
                    <p className="text-xs text-blue-600">Execution Time (Backend)</p>
                    <p className="font-mono text-lg font-bold text-blue-800">
                        {metrics.execution_time_ms} <span className="text-sm font-normal">ms</span>
                    </p>
                </div>

                <div className="pt-4 border-t">
                    <h4 className="font-semibold text-gray-700 mb-2 text-sm">Complexity Analysis</h4>
                    <div className="space-y-2">
                        <div className="flex justify-between items-center text-sm">
                            <span className="text-gray-600">Time Complexity:</span>
                            <span className="font-mono bg-gray-100 px-2 py-1 rounded text-purple-600 font-medium">
                                {complexity.time || '-'}
                            </span>
                        </div>
                        <div className="flex justify-between items-center text-sm">
                            <span className="text-gray-600">Space Complexity:</span>
                            <span className="font-mono bg-gray-100 px-2 py-1 rounded text-green-600 font-medium">
                                {complexity.space || '-'}
                            </span>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    );
};

export default MetricsPanel;
