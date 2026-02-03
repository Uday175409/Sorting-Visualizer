import React, { useState, useEffect, useRef } from 'react';
import Controls from '../components/Controls';
import BarChart from '../components/BarChart';
import MetricsPanel from '../components/MetricsPanel';
import { sortArray } from '../services/api';

const generateRandomArray = (size) => {
    return Array.from({ length: size }, () => Math.floor(Math.random() * 100) + 5);
};

const Visualizer = () => {
    const [algorithm, setAlgorithm] = useState('bubble');
    const [arraySize, setArraySize] = useState(20);
    const [speed, setSpeed] = useState(50);
    const [array, setArray] = useState([]);

    // Visualization State
    const [steps, setSteps] = useState([]);
    const [currentStep, setCurrentStep] = useState(0);
    const [isSorting, setIsSorting] = useState(false);

    // Metrics State
    const [metrics, setMetrics] = useState({ comparisons: 0, swaps: 0, execution_time_ms: 0 });
    const [complexity, setComplexity] = useState({ time: '-', space: '-' });

    // Step Tracking (for coloring)
    // In a real sophisticated visualizer, we might receive diffs. 
    // Here we have full snapshots. We can infer basics or just show the snapshot.
    // To show "active" elements, we would need the backend to return which indices are active.
    // For simplicity in this constraints-based request, we will visualize the array state.
    // Advanced: We could diff steps[i] and steps[i+1] to highlight changes.

    const [activeSwaps, setActiveSwaps] = useState([]);

    const animationRef = useRef(null);

    // Initialize random array
    useEffect(() => {
        handleGenerate();
    }, []);

    // Regenerate when size changes (optional UX choice)
    useEffect(() => {
        handleGenerate();
    }, [arraySize]);

    const handleGenerate = () => {
        if (isSorting) return;
        const newArray = generateRandomArray(arraySize);
        setArray(newArray);
        setSteps([]);
        setCurrentStep(0);
        setMetrics({ comparisons: 0, swaps: 0, execution_time_ms: 0 });
        setComplexity({ time: '-', space: '-' });
        setActiveSwaps([]);
    };

    const handleSort = async () => {
        if (isSorting) return;

        try {
            setIsSorting(true);
            // Call backend
            const response = await sortArray(algorithm, array, "medium");

            // Setup visualization
            setSteps(response.steps);
            setMetrics(response.metrics);
            setComplexity(response.complexity);
            setCurrentStep(0);

            // Start animation loop
            animate(response.steps);

        } catch (error) {
            console.error(error);
            setIsSorting(false);
            alert("Failed to fetch sorting steps from backend.");
        }
    };

    const animate = (allSteps) => {
        let stepIndex = 0;

        const runLoop = () => {
            if (stepIndex >= allSteps.length) {
                setIsSorting(false);
                if (allSteps.length > 0) {
                    setArray(allSteps[allSteps.length - 1]);
                }
                setActiveSwaps([]);
                return;
            }

            const currentArrayState = allSteps[stepIndex];

            // Basic Diff Algorithm to highlight changes (Optional for better visuals)
            // Compare currentArrayState with previous state to find changes
            if (stepIndex > 0) {
                const prevArray = allSteps[stepIndex - 1];
                const diffIndices = [];
                currentArrayState.forEach((val, idx) => {
                    if (val !== prevArray[idx]) {
                        diffIndices.push(idx);
                    }
                });
                setActiveSwaps(diffIndices);
            }

            setArray(currentArrayState);
            setCurrentStep(stepIndex);
            stepIndex++;

            animationRef.current = setTimeout(runLoop, speed);
        };

        runLoop();
    };

    const handleReset = () => {
        clearTimeout(animationRef.current);
        setIsSorting(false);
        handleGenerate();
    };

    // Cancel animation on unmount
    useEffect(() => {
        return () => clearTimeout(animationRef.current);
    }, []);

    return (
        <div className="min-h-screen bg-gray-50 flex flex-col font-sans">
            {/* Header */}
            <header className="bg-white shadow-sm sticky top-0 z-10">
                <div className="max-w-7xl mx-auto px-4 py-4 flex items-center justify-between">
                    <div className="flex items-center space-x-2">
                        <div className="w-8 h-8 bg-blue-600 rounded-md flex items-center justify-center text-white font-bold">
                            AL
                        </div>
                        <h1 className="text-xl font-bold text-gray-800 tracking-tight">
                            DAA Sort Visualizer
                        </h1>
                    </div>
                    <div className="flex items-center space-x-4 text-sm text-gray-500">
                        <span>v1.0.0</span>
                        <a href="#" className="hover:text-blue-600">Documentation</a>
                    </div>
                </div>
            </header>

            <main className="flex-1 max-w-7xl mx-auto px-4 py-8 w-full flex flex-col md:flex-row gap-6">

                {/* Left/Main Column: Visuals & Controls */}
                <div className="flex-1 flex flex-col">
                    <Controls
                        algorithm={algorithm}
                        setAlgorithm={setAlgorithm}
                        arraySize={arraySize}
                        setArraySize={setArraySize}
                        speed={speed}
                        setSpeed={setSpeed}
                        onGenerate={handleGenerate}
                        onSort={handleSort}
                        onReset={handleReset}
                        isSorting={isSorting}
                    />

                    <BarChart
                        array={array}
                        swaps={activeSwaps}
                        // For simplicity, we assume sorted indices are all if finished, or none. 
                        // To be precise we need backend to tell us sorted region.
                        sortedIndices={!isSorting && steps.length > 0 && currentStep >= steps.length - 1 ? array.map((_, i) => i) : []}
                    />

                    {/* Educational Note */}
                    <div className="mt-6 bg-blue-50 border-l-4 border-blue-500 p-4 rounded-r-md">
                        <h4 className="font-bold text-blue-900">How {algorithm} sort works:</h4>
                        <p className="text-blue-800 text-sm mt-1">
                            The backend executes the algorithm step-by-step. Each frame you see represents a state of the array after a comparison or swap operation. The "Comparisons" and "Swaps" counters are updated individually in the algorithm logic.
                        </p>
                    </div>
                </div>

                {/* Right Column: Metrics */}
                <MetricsPanel
                    metrics={metrics}
                    complexity={complexity}
                    algorithm={algorithm}
                />
            </main>
        </div>
    );
};

export default Visualizer;
